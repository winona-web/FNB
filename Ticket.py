# ============================================
# 🎤 GLOBAL HIP-HOP TOUR 2026 - TICKET COUNTER
# ============================================

print("=" * 50)
print("🎤 WELCOME TO THE GLOBAL HIP-HOP TOUR 2026 🎤")
print("Featuring the biggest names in American Hip-Hop!")
print("=" * 50)

# Ask the user for their name
name = input("\nWhat's your name? ")

# Ask for the artist
artist_name = input("Which artist are you seeing? (Drake, Kendrick Lamar, Travis Scott, Future, Nicki Minaj, etc.): ")

# Ask for the number of tickets
num_tickets = int(input("How many tickets would you like to buy? "))

# Ask for the ticket price
ticket_price = float(input("Price per ticket (R): "))

# Calculate total cost
total_cost = num_tickets * ticket_price

# Display total
print(f"\n🎟️ {name}, your total for {num_tickets} ticket(s) is: R{total_cost:.2f}")

# Ask for payment
payment_amount = float(input("Enter your payment amount (R): "))

# Confirmation
print("\n" + "=" * 50)
print(f"🔥 HEY {name.upper()}! 🔥")
print(f"Your tickets to see {artist_name.title()} have been booked successfully!")
print("📍 Venue: Madison Square Garden, New York")
print("🎶 Get ready for an unforgettable night of hip-hop!")
print("=" * 50)

# Check payment
if payment_amount > total_cost:
    change = payment_amount - total_cost
    print(f"✅ Payment received!")
    print(f"💵 Your change is: R{change:.2f}")
    print("🎧 See you in the front row!")

elif payment_amount == total_cost:
    print("✅ Perfect payment received!")
    print("🎤 Enjoy the show and make some memories!")

else:
    amount_owed = total_cost - payment_amount
    print("❌ Payment unsuccessful.")
    print(f"You still owe: R{amount_owed:.2f}")
    print("Please complete your payment to secure your tickets.")

print("\n🌍 Thank you for choosing Global Hip-Hop Tours!")
print("🔥 Stay tuned for upcoming concerts across the USA!")