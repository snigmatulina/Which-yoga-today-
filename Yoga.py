"""Recommends which type of yoga to practice today"""
st.title("What yoga?")

st.write("Answer a few questions and get your yoga style recommendation!")

# Styles of yoga 
hatha = "Hatha yoga"
vinyasa = "Vinyasa yoga"
yin = "Yin yoga"
kundalini = "Kundalini yoga"
ashtanga = "Ashtanga-vinyasa yoga"

# Collect user attributes to inform our recommendation.
energy = st.selectbox("From 1(low) to 5(high) how much energy do you have?", ["1", "2", "3", "4","5"])
speed = st.selectbox("Would you like a slower or faster practice today? ", ["slower", "faster"])
intention = st.selectbox("Is your intention to relax, move, breathe or connect with spiritual part? ", ["relax", "move", "breathe","connect with spiritual part"])
                

# Make a course recommendation based on the user's attributes.
rec = "none"
if energy ==5:
    if speed == "faster":
        rec = vinyasa 
    else: 
        rec = kundalini
elif energy == 4:
    if intention == "breathe":
        rec = kundalini
    else:
        rec = ashtanga
elif energy == 3:
    if intention == "move" or intention == "breathe":
        rec = hatha
    else:
        rec == yin
elif energy == 2:
    if intention =="connect with spiritual part":
        rec = kundalini
    elif intention == "move" or intention == "breathe":
        rec = hatha
    else:
        rec = yin
else:
    if speed == "faster":
        rec = hatha
    else:
        rec=yin
if st.button("Get My Recommendation!"):
   st.markdown(f"### Your recommended :\n**{rec}**")



