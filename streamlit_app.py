# James Mahler (jmahler) and Vivian Lee (vivianle)
import streamlit as st
import pages.home
import pages.player_world_map
import pages.correlations_and_ml

PAGES = {
    'Home': pages.home,
    'Correlations and ML': pages.correlations_and_ml,
    'Player World Map': pages.player_world_map
}


def write_page(page):
    page.write()


def main():

    st.title("Exploring Football Players in FIFA 19")

    st.sidebar.title('Navigation')
    select_page = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[select_page]

    with st.spinner("Loading %s ..." % select_page):
        write_page(page)


if __name__ == "__main__":
    main()
