from .functions.oasDocumentSchema import oasDocumentSchema
from .functions.oasExtGravitee import oasExtGravitee
from .functions.oasOp2xxResponse import oasOp2xxResponse
from .functions.oasOpIdUnique import oasOpIdUnique
from .functions.oasOpParams import oasOpParams

oas_rules = {
    "formats": ["oas2", "oas3"],
    "functions": [
        oasDocumentSchema,
        oasExtGravitee,
        oasOp2xxResponse,
        oasOpIdUnique,
        oasOpParams
    ],
    "rules": {
        "oas2-schema": {
            "description": "Validate structure of OpenAPI v2 specification.",
            "message": "{error}, path: {path}",
            "formats": ["oas2"],
            "severity": "Error",
            "validator": {
                "func": "oasDocumentSchema",
                "args": {
                    "schema": "oas/schemas/schema_oas2.json"
                }
            }
        },
        "oas3-schema": {
            "description": "Validate structure of OpenAPI v3 specification.",
            "message": "{error}, path: {path}",
            "formats": ["oas3"],
            "severity": "Error",
            "validator": {
                "func": "oasDocumentSchema",
                "args": {
                    "schema": "oas/schemas/schema_oas3.json"
                }
            }
        },
        "x-gravitee-schema": {
            "description": "Validate x-gravitee specification.",
            "message": "{error}",
            "formats": ["oas2", "oas3"],
            "severity": "Error",
            "validator": {
                "func": "oasExtGravitee",
                "args": {
                    "schema": "oas/schemas/ext_gravitee/xGraviteeIODefinition.json"
                }
            }
        }
    }
}
