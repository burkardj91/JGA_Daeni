




import streamlit as st
import random


import streamlit as st
st.set_page_config(page_title="Daniele's JGA Game")  # ✅ MUST be first!


# --- Set up page ---
#st.set_page_config(page_title="Daniele's JGA Game", layout="centered")
st.title("\U0001F389 Daniele's JGA Game")
st.info("Das ist ein Spiel für Daniele's Junggesellenabschied! Wähle jeweils eine Frage aus jeder Spalte, erkläre das fette Wort der Gruppe mit 'Erklären' oder 'Pantomime' und erfülle eine lustige Aufgabe.")

# --- Session State Initialization ---
if 'used_cells' not in st.session_state:
    st.session_state.used_cells = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'current_info' not in st.session_state:
    st.session_state.current_info = None
if 'current_mode' not in st.session_state:
    st.session_state.current_mode = None
if 'current_action' not in st.session_state:
    st.session_state.current_action = None
if 'question_step' not in st.session_state:
    st.session_state.question_step = 0

all_actions = [
        "Danieles 'Hotness' Score",
        "Do it like Hal",
        "Danieles 'feminine' Vergangenheit",
]

if 'shuffled_actions' not in st.session_state:
    st.session_state.shuffled_actions = random.sample(all_actions, k=len(all_actions))
if 'used_actions' not in st.session_state:
    st.session_state.used_actions = []

# --- Define Questions with Info ---
questions = {
    '1A': {
        "question": "Danieles illustre Namensvetter",
        "info": ": Der Name stammt aus dem arabisch-arämischen Raum und bedeutet 'Gott ist mein Richter'. Ganz nach diesem Motto hat auch Ian Flemings Kultfigur über Recht gewaltet und noch einige Frauen abgeschleppt. Der letzte Bond war Daniel Craig, und seine Büroflamme heisst <span style='color:#d63384'><b>Monnypenny</b></span>."
    },
    '2A': {
        "question": "Danieles illustre Namensvetter",
        "info": ": Der Name stammt aus dem arabisch-arämischen Raum und bedeutet 'Gott ist mein Richter'. Ganz nach diesem Motto hat auch Harry Potter die Welt wieder zurechtgerichtet. Harrys (gespielt von Daniel Radcliffe) grosser Antagonist hiess <span style='color:#d63384'><b>Voldemort</b></span>."
    },
    '3A': {
        "question": "Danieles illustre Namensvetter",
        "info": ": Der Name stammt aus dem arabisch-arämischen Raum und bedeutet 'Gott ist mein Richter'. Ganz nach diesem Motto hat auch Ian Flemings Kultfigur über Recht gewaltet und noch einige Frauen abgeschleppt. Der letzte Bond war Daniel Craig, und seine Büroflamme heisst <span style='color:#d63384'><b>Monnypenny</b></span>."
    },
    '1B': {
        "question": "Danieles Masterarbeit",
        "info": "Während deiner Masterarbeit wurdest du beauftragt, fortifizierten Reis zu extrudieren – ganz nach der Fuchtel von deiner Betreuerin <span style='color:#d63384'><b>Pornpimol</b></span>."
    },
    '2B': {
        "question": "Danieles Masterarbeit",
        "info": "Während deiner Masterarbeit wurdest du beauftragt, fortifizierten Reis zu extrudieren – ganz nach der Fuchtel von deiner Betreuerin <span style='color:#d63384'><b>Pornpimol</b></span>."
    },
    '3B': {
        "question": "Danieles erstes IT-Projekt",
        "info": "Im ersten Jahr durften wir eine eigene Homepage erstellen, und jeder durfte spannende Infos über den <span style='color:#d63384'><b>Quastenflosser</b></span> lernen."
    },
    '1C': {
        "question": "Danieles Lieblingshobby",
        "info": "Die Velofahrer, umgangssprachlich auch <span style='color:#d63384'><b>Gümmeler</b></span> genannt, sind eine Gruppe von Menschen, die sich dem Velofahren verschrieben haben. Sie sind bekannt für ihre Leidenschaft und Hingabe zum Radfahren."
    },
    '2C': {
        "question": "Winter is Coming",
        "info": "Dieser Satz stammt aus der Serie <span style='color:#d63384'><b>Game of Thrones</b></span> und ist das Motto des Hauses Stark. Die <span style='color:#d63384'><b>Serie</b></span> ist gespickt von Intrigen, Machtkämpfen, epischen Schlachten und Sexszenen. Doch ist diese <span style='color:#d63384'><b>Serie</b></span> allen bekannt?"
    },
    '3C': {
        "question": "Danieles Lieblingshobby",
        "info": "Die Velofahrer, umgangssprachlich auch <span style='color:#d63384'><b>Gümmeler</b></span> genannt, sind eine Gruppe von Menschen, die sich dem Velofahren verschrieben haben. Sie sind bekannt für ihre Leidenschaft und Hingabe zum Radfahren. Aber ist dieser Begriff allen bekannt?"
    },
}


# --- Display Column Headers ---
st.markdown("**Wähle eine Kachel aus:**")
col_titles = st.columns(3)
col_titles[0].markdown("### Facts")
col_titles[1].markdown("### Science")
col_titles[2].markdown("### Leisure")

# --- Create 3x3 Button Grid ---
for row in range(1, 4):
    cols = st.columns(3)
    for col_idx, col in enumerate(cols):
        cell = f"{row}{chr(65 + col_idx)}"
        if cell in st.session_state.used_cells:
            col.button(cell, disabled=True, key=f"btn_{cell}")
        else:
            if col.button(cell, key=f"btn_{cell}"):
                q = questions[cell]
                st.session_state.current_question = q["question"]
                st.session_state.current_info = q["info"]
                st.session_state.used_cells.append(cell)
                st.session_state.current_mode = random.choice(['Erklären', 'Pantomime'])
                remaining = [a for a in st.session_state.shuffled_actions if a not in st.session_state.used_actions]
                chosen = remaining[0] if remaining else "Do it like Hal"
                st.session_state.used_actions.append(chosen)
                st.session_state.current_action = chosen
                st.session_state.question_step = 1

# --- Step 1: Show Question ---
if st.session_state.question_step >= 1:
    st.markdown(f"**Frage:** {st.session_state.current_question}")
    st.markdown(f"<span style='color:gray; font-size: 0.9em;'>ℹ️ {st.session_state.current_info}</span>", unsafe_allow_html=True)
    if st.button("Reveal Mode", key="reveal_mode"):
        st.session_state.question_step = 2

# --- Step 2: Show Mode ---
if st.session_state.question_step >= 2:
    st.markdown(f"**Modus:** {st.session_state.current_mode}")
    if st.button("Reveal Action", key="reveal_action"):
        st.session_state.question_step = 3

# --- Step 3: Show Action ---
if st.session_state.question_step == 3:
    action = st.session_state.current_action
    st.success(f"**Your Action:** {action}")

    if action == "Danieles 'feminine' Vergangenheit":
        try:
            st.image("WhatsApp Bild 2025-07-04 um 16.58.53_10eb151a.jpg", caption="🐱📦", use_container_width=True)
        except Exception:
            st.info("Image not found. Make sure the image file is in the same folder.")
        st.markdown("Frage mind. fünf Fussgänger (fremd), ob Sie mit den Schönheitseingriffen von Daniele zufrieden sind.")


    elif action == "Danieles 'Hotness' Score":
        try:
            st.image("WhatsApp Bild 2025-07-04 um 20.35.52_55f6e13b.jpg", caption="🌶🔥🫠", use_container_width=True)
        except Exception:
            st.info("Image not found. Make sure the image file is in the same folder.")
        st.markdown("Die Temperaturen sind heiss, und das bist du natürlich auch. Für uns bist du eine 10 - doch für deine Libido ist eine externe Evaluation hilfreich. Lass dich von 5 fremden Leuten auf der Attraktivitätsskala von 1-10 einstufen.")

    elif action == "Do it like Hal":
        st.video("https://www.youtube.com/watch?v=sUcgl_dOrR8")  
        st.markdown("Seine Tanzkünste sind legendär. Zeige uns deine besten Moves! Ganz nach dem Motto: 'Do it like Hal'.")

    if st.button("Zurück zum Spielfeld"):
        st.session_state.current_question = None
        st.session_state.current_info = None
        st.session_state.current_mode = None
        st.session_state.current_action = None
        st.session_state.question_step = 0

# --- Optional: End Message ---
if len(st.session_state.used_cells) == 9 and st.session_state.question_step == 0:
    st.success("🎉 Das Spiel ist beendet! Alle Fragen wurden beantwortet. Zeit zu feiern!")
