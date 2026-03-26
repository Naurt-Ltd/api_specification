import {
	Configuration,
	FinalDestinationApi,
	FinalDestinationRequest,
	FinalDestinationResponse,
	ResponseError,
} from "@naurt/api";
import * as fs from "fs";

const apiKey = fs.readFileSync("../api.key", "utf-8").trim();

async function main(): Promise<void> {
	const request: FinalDestinationRequest = {
		queries: [
			{
				id: "8bd197aa-7328-3e10-9ea7-7ec139e9fa48",
			},
		],
	};

	const config = new Configuration({
		basePath: "https://api.naurt.net",
		apiKey: async (name: string): Promise<string | undefined> => {
			if (name === "Authorization") {
				return apiKey;
			}
			return undefined;
		},
	});

	const api = new FinalDestinationApi(config);

	try {
		const raw = await api.finaldestinationPostRaw({
			finalDestinationRequest: request,
		});

		const data: FinalDestinationResponse = await raw.value();
		console.log(JSON.stringify(data, null, 2));
	} catch (err: unknown) {
		console.error("error:", err);

		if (err instanceof ResponseError) {
			const text = await err.response.text();
			console.error("raw body:", text);
			return;
		}

		if (
			typeof err === "object" &&
			err !== null &&
			"response" in err &&
			err.response instanceof Response
		) {
			const text = await err.response.text();
			console.error("raw body:", text);
		}
	}
}

main().catch((err: unknown) => {
	console.error(err);
	process.exit(1);
});