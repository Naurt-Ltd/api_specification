
# RendezvousQuery

Shared Naurt Query object.  The Rendezvous spec refers to the shared Search Query specification. At minimum, address-based queries such as `address_string` are supported. Other shared query forms may also be accepted. 

## Properties

Name | Type
------------ | -------------
`addressString` | string
`latitude` | number
`longitude` | number

## Example

```typescript
import type { RendezvousQuery } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "addressString": null,
  "latitude": null,
  "longitude": null,
} satisfies RendezvousQuery

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RendezvousQuery
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


