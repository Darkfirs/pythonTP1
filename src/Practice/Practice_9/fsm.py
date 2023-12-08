from dataclasses import dataclass
from typing import Dict, List


@dataclass
class FSMachine:
    states: List[Dict[str, int]]
    start_state: int
    accepted_states: List[int]


def create_fs_machine(
    given_states: List[Dict[str, int]], start_state: int, accepted_states: List[int]
) -> FSMachine:
    all_states = list(given_states)
    return FSMachine(all_states, start_state, accepted_states)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_state = fsm.start_state
    for symbol in string:
        current_state_data = fsm.states[current_state]
        next_state_candidates = [
            next_state
            for condition, next_state in current_state_data.items()
            if symbol in condition
        ]
        if not next_state_candidates:
            return False
        current_state = next_state_candidates[0]
    return current_state in fsm.accepted_states
