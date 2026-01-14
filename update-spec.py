#
# Copyright 2019-Present Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import requests
import sys

from datetime import datetime
from yaml import dump as yaml_dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


GUIDE_API_TOKEN = os.getenv("GUIDE_API_TOKEN")
GUIDE_VERSION = datetime.now().strftime("%Y%m")

if GUIDE_API_TOKEN is None or GUIDE_API_TOKEN == '':
    print(f'No Sonatype Guide API token set in GUIDE_API_TOKEN environment variable.')
    sys.exit(0)

json_spec_response = requests.get('https://api.guide.sonatype.com/.well-known/api-catalog', headers={
    "Authorization": f"Bearer {GUIDE_API_TOKEN}"
})
json_spec = json_spec_response.json()

# Update OpenAPI Info Block
print('Updating `info`')
json_spec['info'] = {
    'title': 'Sonatype Guide API',
    'description': 'REST API into [Sonatype Guide]'
                   '(https://guide.sonatype.com).',
    'contact': {
        'name': 'Sonatype Community Maintainers',
        'url': 'https://github.com/sonatype-nexus-community'
    },
    'license': {
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
    },
    'version': GUIDE_VERSION
}

# Update Servers
print('Updating `servers`')
json_spec['servers'] = [
    {
        'description': 'Production',
        'url': 'https://api.guide.sonatype.com'
    }
]

with open('./spec/openapi.yaml', 'w') as output_yaml_specfile:
    output_yaml_specfile.write(yaml_dump(json_spec))
