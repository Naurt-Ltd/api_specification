import { Configuration, FinalDestinationApi } from "@naurt/api";

const fs = require('fs');

const api_key = fs.readFileSync("../api.key", "utf-8");

async function main() {
	const config = new Configuration({
		basePath: "https://api.naurt.net",
		apiKey: async (name) => {
			if (name === "Authorization") {
				return api_key
			}
			return undefined
		},
	});

	const api = new FinalDestinationApi(config);

	const raw = await api.finaldestinationPostRaw({
		finalDestinationRequest: {
			queries: [
				{
					addressString: "447 Digby Rd, Evesham WR11 1BW",
				},
			],
		},
	})

	try {
		const data = await raw.value()
		console.log(JSON.stringify(data, null, 2))

	} catch (err) {
		console.error("error:", err)

		if (err?.response) {
			const text = await err.response.text()
			console.error("raw body:", text)
		}
	}
};

main().catch((err) => {
	console.error(err)
	process.exit(1)
});