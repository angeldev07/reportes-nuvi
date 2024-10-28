import requests
from house_report import HouseReport

houseReportObj = HouseReport(path="2024-10-OCTUBRE IBIZA.xlsx")
houses = [house.to_nuvi() for house in houseReportObj.gethousesreport()]


url = "http://localhost:3000/api/general/condominio/report-properties"

data = {"nit": "9009886810", "properties": houses}

res = requests.post(url, json=data).json()

print(res)
