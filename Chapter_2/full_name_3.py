# Step 2 — Run full_name_3.py
first_name = "lesedi"
last_name = "skaki"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)

# Step 4 — Break it on purpose (SyntaxError)
# Before changing:
message = "One of Python's strengths is its diverse community."
print(message)

#After changing:
# message = 'One of Python's strengths is its diverse community.'
# print(message)