#  Copyright 2022 Token Flow Insights
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under
#  the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
#  OF ANY KIND, either express or implied.
#
#  See the License for the specific language governing permissions and limitations
#  under the License.
#
#  The product contains trademarks and other branding elements of Token Flow Insights SA
#  which are not licensed under the Apache 2.0 license. When using or reproducing the code,
#  please remove the trademark and/or other branding elements.
#

from typing import Optional
import json
from flask import Blueprint, render_template, request
from app.engine.decoders.trace import decode_trace

from app.engine.decoders.transaction import decode_transaction
from app.engine.providers.sequencer import (
    get_transaction,
    get_block_hash,
    get_transaction_trace,
)
from app.frontend import frontend_route

bp = Blueprint("simulation", __name__)

@frontend_route(bp, "/inspect/")
def route_simulation() -> tuple["render_template", int]:
    raw_trace = json.loads(request.args.get('trace')).get('trace').get('function_invocation')
    chain_id = 'testnet'
    block_hash = 'pending'
    [decoded_trace, decoded_events] = decode_trace(chain_id, block_hash, raw_trace, None, 4)
    # decoded_trace = trace
    return render_template(
        "simulation.html",
        chain_id=chain_id,
        trace=json.dumps(raw_trace, indent=4),
        decoded_trace_json=json.dumps(decoded_trace, indent=6),
        decoded_trace=decoded_trace,
        decoded_events=decoded_events
    ), 200
