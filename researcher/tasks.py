from researcher.methods import generate_business_profile, generate_queries, research
from huey.contrib.djhuey import task

@task()
def process_research(company_name):
    queries = []

    financial_queries = generate_queries("Finance", company_name)
    leadership_queries = generate_queries("Leadership", company_name)
    operations_queries = generate_queries("Operations", company_name)
    corporate_history_queries = generate_queries("Corporate History", company_name)

    queries.extend(financial_queries.get("queries"))
    queries.extend(leadership_queries.get("queries"))
    queries.extend(operations_queries.get("queries"))
    queries.extend(corporate_history_queries.get("queries"))

    context = ""

    for query in queries:
        response = research(query)
        context += f"Query : {query} \nResponse : {response} \n\n"

    business_profile = generate_business_profile(context)
        
    print(business_profile)