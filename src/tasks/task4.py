from typing import Any
from to_do import TODO
def task4(projects: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:

    result = {}

    for project,details in projects.items():
        project_id = details["project-id"]
        costs = details["costs"]

        new_costs = []

        for cost in costs:
            if cost is None:
                new_costs.append(-10.0)
            else:
                new_costs.append(cost * 2)

        result[project] = {"project-id": project_id,"costs": new_costs}

    return result

if __name__ == "__main__":

    print(task4(projects={"Alpha":{"project-id":11,"costs": [1200.0,None, 950.0,None]},"Beta":{"project-id":22,"costs":[None, 800.0,None, 700.0]},"Gamma":{"project-id":33,"costs":[600.0,None,None,500.0]}}))