from applications import add_applications

application_id = add_applications(
    company="Microsoft",
    role="Software Engineer",
    status="applied"
)

print(f"Application added with ID: {application_id}")