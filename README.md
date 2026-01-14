# Sonatype Guide API Client(s)

<!-- Badges Section -->

[![shield_gh-workflow-test]][link_gh-workflow-test]
[![shield_license]][license_file]

<!-- Add other badges or shields as appropriate -->

---

This repository produces generated API Clients for [Sonatype Guide](https://guide.sonatype.com) in various languages and frameworks for use by Customers and other projects.

- [Supported Languages \& Frameworks](#supported-languages--frameworks)
- [Customisations](#customisations)
- [Getting the latest OpenAPI Schema](#getting-the-latest-openapi-schema)
- [Generation of API Clients](#generation-of-api-clients)
- [Releasing](#releasing)
- [The Fine Print](#the-fine-print)

## Supported Languages & Frameworks

_Request a new lanaguage / framework via GitHub Issue._

| Language / Framework | Sonatype Guide Version Added | Public Package Link                                                                                                                                                                                       |
| -------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Golang / Go          | 14-Jan-2026 _(`1.202601.0`)_ | [![go.dev reference](https://img.shields.io/github/v/tag/sonatype-nexus-community/sonatype-guide-api-client-go)](https://pkg.go.dev/github.com/sonatype-nexus-community/sonatype-guide-api-client-go)             |
| Java (Webclient)     | 14-Jan-2026 _(`1.202601.0`)_ | [![Maven Central Version](https://img.shields.io/maven-central/v/org.sonatype.community/sonatype-guide-api-webclient)](https://central.sonatype.com/artifact/org.sonatype.community/sonatype-guide-api-webclient) |
| Python               | 14-Jan-2026 _(`1.202601.0`)_ | [![PyPi](https://img.shields.io/pypi/v/sonatype_guide_api_client)](https://pypi.org/project/sonatype_guide_api_client/)                                                                                                     |
| Typescript (fetch)   | 14-Jan-2026 _(`1.202601.0`)_ | [![npm](https://img.shields.io/npm/v/@sonatype/sonatype-guide-api-client)](https://www.npmjs.com/package/@sonatype/sonatype-guide-api-client)                                                                 |

## Customisations

There are a small number of customisations to the published OpenAPI specification. These are captured in the `update-spec.py` script.

## Getting the latest OpenAPI Schema

Use your Guide API Token to access the latest OpenAPI schema:

```
curl -H 'Authorization: Bearer <YOUR-GUIDE-API-TOKEN>' https://api.guide.sonatype.com/.well-known/api-catalog > spec/openapi.yaml
```

## Generation of API Clients

Example:

```
docker run --rm -v "$(PWD):/local" openapitools/openapi-generator-cli batch --clean /local/typescript.yaml
```

## Releasing

As Sonatype Guide is a Cloud service, we version API clients based on year, month and fix (patch) version.

For example - an OpenAPI spec fetched on 5th March 2026 might be version `1.202603.0.`

Adding git tags triggers the release process.

## The Fine Print

Remember:

This project is part of the [Sonatype Nexus Community](https://github.com/sonatype-nexus-community) organization, which is not officially supported by Sonatype. Please review the latest pull requests, issues, and commits to understand this project's readiness for contribution and use.

-   File suggestions and requests on this repo through GitHub Issues, so that the community can pitch in
-   Use or contribute to this project according to your organization's policies and your own risk tolerance
-   Don't file Sonatype support tickets related to this project— it won't reach the right people that way

Last but not least of all - have fun!

<!-- Links Section -->

[shield_gh-workflow-test]: https://img.shields.io/github/actions/workflow/status/sonatype-nexus-community/sonatype-guide-api-client/test.yml?branch=main&logo=GitHub&logoColor=white 'build'
[shield_license]: https://img.shields.io/github/license/sonatype-nexus-community/sonatype-guide-api-client?logo=open%20source%20initiative&logoColor=white 'license'
[link_gh-workflow-test]: https://github.com/sonatype-nexus-community/sonatype-guide-api-client/actions/workflows/test.yml?query=branch%3Amain
[license_file]: https://github.com/sonatype-nexus-community/sonatype-guide-api-client/blob/main/LICENSE
