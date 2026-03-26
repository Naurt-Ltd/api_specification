from naurt_api import AuthenticatedClient
from naurt_api.api.final_destination import finaldestination_post
import naurt_api.models as naurt_models
from uuid import UUID

f = open("api.key", "r")
API_KEY = f.read()
f.close()

def main():
	client = AuthenticatedClient(
		base_url="https://api.naurt.net",
		token=API_KEY,
		prefix="" # NOTE: This is important
	)

	queries = [
		naurt_models.FinalDestinationQuery(
			source_id=naurt_models.FinalDestinationSourceIdRequest(os_uprn="200001191298")
		),
		naurt_models.FinalDestinationQuery(address_string="47 Digby Rd, Evesham WR11 1BW"),
		naurt_models.FinalDestinationQuery(location=naurt_models.FinalDestinationLocation(latitude=51.484, longitude=-0.607)),
	]

	request = naurt_models.FinalDestinationRequest(queries=queries)

	response = finaldestination_post.sync(client=client, body=request)

	print(response)


if __name__ == "__main__":
	main()