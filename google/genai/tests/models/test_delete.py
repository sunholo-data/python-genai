# Copyright 2024 Google LLC
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


"""Tests for models.get."""

import pytest

from ... import errors
from ... import types
from .. import pytest_helper


test_table: list[pytest_helper.TestTableItem] = [
    pytest_helper.TestTableItem(
        name='test_delete_model',
        parameters=types._DeleteModelParameters(
            model='models/8533706666867163136'
        ),
        exception_if_mldev='404',
    ),
    pytest_helper.TestTableItem(
        name='test_delete_tuned_model',
        parameters=types._DeleteModelParameters(
            model='tunedModels/generate-num-9598'
        ),
        exception_if_vertex='404',
    ),
]
pytestmark = pytest_helper.setup(
    file=__file__,
    globals_for_file=globals(),
    test_method='models.delete',
    test_table=test_table,
)


@pytest.mark.asyncio
async def test_async_delete_tuned_model(client):
  if client._api_client.vertexai:
    with pytest.raises(errors.ClientError) as e:
      await client.aio.models.delete(model='tunedModels/generate-num-888')
      assert '404' in str(e)
  else:
    response = await client.aio.models.delete(
        model='tunedModels/generate-num-888'
    )


@pytest.mark.asyncio
async def test_async_delete_model(client):
  if client._api_client.vertexai:
    response = await client.aio.models.delete(
        model='models/1071206899942162432'
    )
  else:
    with pytest.raises(errors.ClientError) as e:
      await client.aio.models.delete(model='models/1071206899942162432')
      assert '404' in str(e)
