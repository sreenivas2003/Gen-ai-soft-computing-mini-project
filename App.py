import streamlit as st
from generate import generate_music
import pretty_midi
import matplotlib.pyplot as plt

st.title("🎵 AI Music Generator with Soft Computing")

# 🎯 Inputs
mood = st.selectbox("Choose Mood", ["happy", "sad", "relax", "energetic", "calm"])
instrument_name = st.selectbox(
    "Instrument",
    ["Acoustic Grand Piano", "Acoustic Guitar (nylon)", "Violin"]
)

# 🎯 Soft Computing Input
mood_level = st.slider("Energy Level (Soft Computing)", 0.0, 1.0, 0.5)

# 📊 Piano Roll
def plot_piano_roll(midi_file):
    pm = pretty_midi.PrettyMIDI(midi_file)
    piano_roll = pm.get_piano_roll()

    fig, ax = plt.subplots()
    ax.imshow(piano_roll, aspect='auto', origin='lower')
    ax.set_title("Piano Roll")
    ax.set_xlabel("Time")
    ax.set_ylabel("Pitch")

    st.pyplot(fig)

# 📊 Note Distribution
def plot_note_distribution(midi_file):
    pm = pretty_midi.PrettyMIDI(midi_file)

    notes = []
    for instrument in pm.instruments:
        for note in instrument.notes:
            notes.append(note.pitch)

    fig, ax = plt.subplots()
    ax.hist(notes, bins=20)
    ax.set_title("Note Distribution")
    ax.set_xlabel("Pitch")
    ax.set_ylabel("Count")

    st.pyplot(fig)

# ▶️ Generate
if st.button("Generate Music"):
    file = generate_music(mood, 120, instrument_name, mood_level)

    st.success("Music Generated!")

    # Download
    with open(file, "rb") as f:
        st.download_button("Download Music", f, file_name="music.mid")

    # Graphs
    st.subheader("📊 Music Visualizations")
    plot_piano_roll(file)
    plot_note_distribution(file)
