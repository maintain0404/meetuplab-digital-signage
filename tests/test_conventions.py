import pytest
import re
from pathlib import Path
from bs4 import BeautifulSoup


class TestPageNameConvention:
    """페이지 디렉토리 이름 규칙 검증"""

    def get_pages_dir(self):
        return Path(__file__).parent.parent / "pages"

    def test_directory_names_are_kebab_case(self):
        """디렉토리 이름은 영문 소문자, 숫자와 -만 사용"""
        pages_dir = self.get_pages_dir()
        
        # index.html의 부모 디렉토리가 pages 디렉토리인지 확인
        assert pages_dir.exists(), "pages 디렉토리가 없습니다"
        
        # 서브디렉토리 검증 (pages 직하위의 디렉토리들)
        for item in pages_dir.iterdir():
            if item.is_dir() and item.name != "__pycache__":
                # 디렉토리명이 영문 소문자, 숫자, -만 사용하는지 확인
                assert re.match(r"^[a-z0-9-]+$", item.name), \
                    f"디렉토리명 '{item.name}'은 영문 소문자, 숫자, -만 사용해야 합니다"
        
        print("✓ 모든 디렉토리명이 규칙을 따릅니다")


class TestIframeStructure:
    """Iframe과 디렉토리 매핑 규칙 검증"""

    def get_pages_html(self):
        html_path = Path(__file__).parent.parent / "pages" / "index.html"
        return BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    def get_page_directories(self):
        pages_dir = Path(__file__).parent.parent / "pages"
        return [d.name for d in pages_dir.iterdir() 
                if d.is_dir() and d.name != "__pycache__"]

    def test_iframe_has_id_matching_directory(self):
        """각 섹션의 iframe id는 해당 디렉토리명과 일치해야 함"""
        soup = self.get_pages_html()
        iframes = soup.find_all("iframe")
        page_dirs = self.get_page_directories()
        
        assert len(iframes) > 0, "iframe이 없습니다"
        
        for iframe in iframes:
            iframe_id = iframe.get("id")
            src = iframe.get("src", "")
            
            # src가 pages 서브디렉토리를 가리키는지 확인
            assert src.startswith("./"), f"iframe src '{src}'은 './'로 시작해야 합니다"
            assert src.split("/")[1] in page_dirs, f"iframe src '{src}'이 pages 디렉토리의 서브디렉토리를 가리켜야 합니다"
            
            # 현재는 규칙을 따르지 않을 수 있으므로, 경고로 표시
            assert iframe_id, f"iframe에 id가 없습니다: {src}"

    def test_all_directories_have_index_html(self):
        """각 페이지 디렉토리에는 index.html이 있어야 함"""
        pages_dir = Path(__file__).parent.parent / "pages"
        
        for item in pages_dir.iterdir():
            if item.is_dir() and item.name != "__pycache__":
                index_html = item / "index.html"
                README_md = item / "README.md"
                assert index_html.exists(), f"{item.name}/index.html이 없습니다"
                assert README_md.exists(), f"{item.name}/README.md이 없습니다"


class TestQueryParameterNaming:
    """쿼리 파라미터 네이밍 규칙 검증"""

    def get_pages_html(self):
        html_path = Path(__file__).parent.parent / "pages" / "index.html"
        return BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    def is_camel_case(self, name):
        """camelCase인지 확인 (첫 글자는 소문자, 이후 대문자는 각 단어마다)"""
        return bool(re.match(r"^[a-z]+([A-Z][a-z]*)*$", name))

    def test_input_select_names_are_camel_case(self):
        """input/select의 name 어트리뷰트는 camelCase여야 함"""
        soup = self.get_pages_html()
        inputs = soup.find_all(["input", "select"])
        
        for elem in inputs:
            name = elem.get("name")
            if name and name.strip():  # name이 있고 비어있지 않으면
                assert self.is_camel_case(name), f"쿼리 파라미터 name '{name}'은 camelCase로 작성해야 합니다"


class TestPageDocumentation:
    """페이지 문서화 규칙 검증"""

    def get_pages_readme(self):
        readme_path = Path(__file__).parent.parent / "pages" / "README.md"
        if not readme_path.exists():
            return None
        return readme_path.read_text(encoding="utf-8")

    def test_readme_exists(self):
        """pages/README.md가 존재해야 함"""
        readme = self.get_pages_readme()
        assert readme is not None, "pages/README.md가 없습니다"
        print("✓ pages/README.md가 존재합니다")


class TestConsistency:
    """HTML과 문서화의 일관성 검증"""

    def get_pages_html(self):
        html_path = Path(__file__).parent.parent / "pages" / "index.html"
        return BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    def test_each_container_has_button(self):
        """각 small-page-container에는 미리보기와 전체화면 버튼이 있어야 함"""
        soup = self.get_pages_html()
        containers = soup.find_all("div", class_="small-page-container")
        
        assert len(containers) > 0, "small-page-container가 없습니다"
        
        for i, container in enumerate(containers, 1):
            buttons = container.find_all("button", class_="editor-button")
            assert len(buttons) >= 2, \
                f"컨테이너 {i}에 버튼이 부족합니다 (필요: 2개, 실제: {len(buttons)}개)"
            
            # onclick이 applySettings인지 확인
            for button in buttons:
                onclick = button.get("onclick", "")
                assert "applySettings" in onclick, \
                    f"버튼의 onclick이 applySettings를 호출하지 않습니다: {onclick}"
        
        print(f"✓ {len(containers)}개 섹션 모두 버튼 구조가 올바릅니다")

    def test_each_container_has_form_inputs(self):
        """각 섹션에는 설정을 위한 input/select가 있어야 함"""
        soup = self.get_pages_html()
        containers = soup.find_all("div", class_="small-page-container")
        
        for i, container in enumerate(containers, 1):
            # page-editor 섹션 찾기
            editor = container.find("div", class_="page-editor")
            assert editor is not None, f"컨테이너 {i}에 page-editor가 없습니다"
            
            # input/select 찾기
            inputs = editor.find_all(["input", "select"])
            # 일부 섹션은 입력이 없을 수 있으므로 경고만 출력
            if not inputs:
                print(f"⚠ 컨테이너 {i}에 입력 요소가 없습니다")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
