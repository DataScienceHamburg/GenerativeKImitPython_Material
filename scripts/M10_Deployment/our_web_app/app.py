#%% packages
import streamlit as st
from helper_funs import get_movies_from_plot
# %%
st.write("Beschreibe die Handlung")

# Chat input for plot description
if user_input := st.chat_input("Beschreibe die Handlung..."):
    user_input = user_input.strip()
    if len(user_input) < 3:
        st.info("Bitte gib eine aussagekräftige Handlungsbeschreibung ein (mind. 3 Zeichen).")
    else:
        with st.spinner("Suche Filme..."):
            data = get_movies_from_plot(user_input)

        # Error handling
        if data.get("error"):
            st.error(f"Fehler bei der Abfrage: {data['error']}")
        else:
            movies = data.get("movies", [])
            if not movies:
                st.warning("Keine Filme gefunden.")
            else:
                for index, movie in enumerate(movies):
                    st.markdown(f"**{movie.get('title', '')}**")
                    st.write(f"Darsteller: {movie.get('main_characters', '')}")
                    st.write(f"Regisseur: {movie.get('director', '')}")
                    st.write(f"Veröffentlichungsjahr: {movie.get('release_year', '')}")
                    if index < len(movies) - 1:
                        st.divider()