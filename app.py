import os
from dotenv import load_dotenv
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")


transport = RequestsHTTPTransport(
    url='https://api.github.com/graphql',
    headers={'Authorization': f'Bearer {TOKEN}'},
    use_json=True
)

client = Client(transport=transport, fetch_schema_from_transport=True)


USERNAME = "HarshilxAI"


query = gql(f"""
{{
  user(login: "{USERNAME}") {{
    contributionsCollection {{
      contributionCalendar {{
        weeks {{
          contributionDays {{
            date
            contributionCount
          }}
        }}
      }}
    }}
  }}
}}
""")

# Run the query
result = client.execute(query)

# Print some results
print("✅ Contribution data fetched!\n")

# Flatten the calendar data
contributions = []
weeks = result['user']['contributionsCollection']['contributionCalendar']['weeks']
for week in weeks:
    for day in week['contributionDays']:
        date = day['date']
        count = day['contributionCount']
        contributions.append((date, count))

# Print last 7 days
print("Last 7 days of contributions:")
for day in contributions[-7:]:
    print(day)

from streak_utils import calculate_streaks

# Calculate and display streak data
stats = calculate_streaks(contributions)

print(f"\n🔥 Current Streak: {stats['current_streak']} days")
print(f"🏆 Longest Streak: {stats['longest_streak']} days")
print(f"📅 From: {stats['longest_start']} to {stats['longest_end']}")
print(f"➕ Total Contributions: {stats['total_contributions']} commits")

import json

# Save JSON output for the frontend
with open("web/data.json", "w") as f:
    json.dump(stats, f, default=str)
