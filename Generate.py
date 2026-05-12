import pretty_midi
import numpy as np

def generate_music(mood="happy", tempo=120, instrument_name="Acoustic Grand Piano", mood_level=0.5):
    
    # 🎯 Soft Computing: Fuzzy-like tempo control
    # mood_level: 0 (calm) → 1 (energetic)
    tempo = int(60 + mood_level * 100)

    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

    program = pretty_midi.instrument_name_to_program(instrument_name)
    instrument = pretty_midi.Instrument(program=program)

    # 🎵 Mood-based scales
    if mood == "happy":
        scale = [60, 62, 64, 67, 69]
    elif mood == "sad":
        scale = [60, 62, 63, 65, 67]
    elif mood == "relax":
        scale = [60, 64, 67]
    elif mood == "energetic":
        scale = [60, 64, 67, 72, 76]
    elif mood == "calm":
        scale = [60, 62, 65, 69]
    else:
        scale = [60, 62, 64]

    start = 0

    # 🎯 Soft Computing: Probability-based note selection
    weights = np.linspace(0.2, 1.0, len(scale))
    weights = weights / weights.sum()

    for i in range(30):
        pitch = np.random.choice(scale, p=weights)

        # Duration depends on energy (soft logic)
        if mood_level > 0.6:
            duration = np.random.uniform(0.2, 0.5)
        else:
            duration = np.random.uniform(0.5, 1.0)

        note = pretty_midi.Note(
            velocity=100,
            pitch=int(pitch),
            start=start,
            end=start + duration
        )

        instrument.notes.append(note)
        start += duration

    pm.instruments.append(instrument)

    output_file = "output.mid"
    pm.write(output_file)

    return output_file
