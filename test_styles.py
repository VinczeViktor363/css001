import pytest

@pytest.fixture
def css_content():
    """Beolvassa a styles.css fájl tartalmát."""
    with open("styles.css", "r", encoding="utf-8") as file:
        return file.read().strip()

def test_styles_not_empty(css_content):
    """Ellenőrzi, hogy a styles.css fájl nem üres."""
    assert css_content, "A styles.css fájl nem lehet üres!"

def test_background_color(css_content):
    """Ellenőrzi, hogy az oldalhoz háttérszín van beállítva."""
    assert "background" in css_content, "Nem található háttérszín beállítás."

def test_title_centered(css_content):
    """Ellenőrzi, hogy a főcím középre van igazítva és nagyobb betűmérettel rendelkezik."""
    assert "text-align: center" in css_content or "justify-content: center" in css_content, "A főcím nincs középre igazítva."
    assert "font-size" in css_content, "A főcím mérete nincs megadva."

def test_navbar_styling(css_content):
    """Ellenőrzi, hogy a navigációs menü formázása megfelelő."""
    assert "display: flex" in css_content or "display: inline-block" in css_content, "A navigációs menü nincs vízszintes sorba rendezve."
    assert ":hover" in css_content and "color" in css_content, "A hover állapot nincs megfelelően beállítva a linkekre."

def test_paragraph_font(css_content):
    """Ellenőrzi, hogy a bekezdések betűtípusa megfelelő."""
    assert "font-family" in css_content, "A bekezdések betűtípusa nincs megadva."

def test_layout(css_content):
    """Ellenőrzi, hogy CSS Grid vagy Flexbox elrendezés van használva."""
    assert "display: grid" in css_content or "display: flex" in css_content, "Nem használtál CSS Grid-et vagy Flexbox-ot az elrendezéshez."

def test_section_styling(css_content):
    """Ellenőrzi, hogy a 'Feladatok' szekciónak van kerete és háttérszíne."""
    assert "border" in css_content, "A 'Feladatok' szekció nem rendelkezik kerettel."
    assert "background" in css_content, "A 'Feladatok' szekció nem rendelkezik háttérszínnel."

def test_footer_content(css_content):
    """Ellenőrzi, hogy a lábléc tartalmazza a nevet és az évszámot."""
    assert "footer" in css_content, "A lábléc nincs definiálva."
    assert "2025" in css_content or "2024" in css_content, "A lábléc nem tartalmazza az évszámot."
