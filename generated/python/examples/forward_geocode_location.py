from naurt_api import AuthenticatedClient
from naurt_api.api.final_destination import finaldestination_post
import naurt_api.models as naurt_models

f = open("api.key", "r")
API_KEY = f.read()
f.close()

def main():
	client = AuthenticatedClient(
		base_url="https://api.naurt.net",
		token=API_KEY,
		prefix="" # NOTE: This is important
	)

	query = naurt_models.FinalDestinationQuery(
		address_string="32 Thames St, Windsor SL4 1PS",
		location=naurt_models.FinalDestinationLocation(latitude=51.484, longitude=-0.607)
	)

	request = naurt_models.FinalDestinationRequest(queries=[query])

	response = finaldestination_post.sync(client=client, body=request)

	print(response)


if __name__ == "__main__":
	main()