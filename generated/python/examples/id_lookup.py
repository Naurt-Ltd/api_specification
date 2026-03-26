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

	query = naurt_models.FinalDestinationQuery(
		id=UUID('8bd197aa-7328-3e10-9ea7-7ec139e9fa48')
	)

	request = naurt_models.FinalDestinationRequest(queries=[query])

	response = finaldestination_post.sync(client=client, body=request)

	print(response)


if __name__ == "__main__":
	main()