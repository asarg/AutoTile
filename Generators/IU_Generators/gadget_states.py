from UniversalClasses import State, AffinityRule, System, TransitionRule, Tile, Assembly
from Assets.colors import *
from binary_symbols_colors import check_point_sym


signal_enter_inactive = State("SignalEnterInactive", signal_inactive_color, "⎆⍼")
signal_exit_inactive = State("SignalExitInactive", signal_inactive_color, "⎋⍼")
signal_enter_active = State("SignalEnterActive", signal_active_color, "⎆⍼")
signal_exit_accept = State("SignalExitAccept", signal_full_accept_color, "⎋⍼")
signal_checkpoint_inactive = State("SignalCheckpointInactive", signal_inactive_color, "{}⍼".format(check_point_sym))
signal_checkpoint_active = State("SignalCheckpointActive", signal_active_color, "{}⍼".format(check_point_sym))
signal_checkpoint_reject = State("SignalCheckpointReject", signal_reject_color, "{}⍼".format(check_point_sym))
signal_checkpoint_accept = State("SignalCheckpointAccept", signal_full_accept_color, "{}⍼".format(check_point_sym))
signal_conditional_full_reject = State("SignalConditionalFullReject", signal_reject_color, "⍼✖")
signal_enter_states = [signal_enter_active, signal_enter_inactive]
signal_exit_states = [signal_exit_accept, signal_exit_inactive]
signal_checkpoint_states = [signal_checkpoint_inactive, signal_checkpoint_active, signal_checkpoint_reject, signal_checkpoint_accept]
signal_receiver_inactive = State("SignalReceiverInactive", signal_inactive_color, "⎆", "black")
signal_received_accept = State("SignalReceivedAccept", signal_full_accept_color, "⚡✔✔", "black")
signal_received_reject = State("SignalReceivedReject", reject_color, "✖⚡", "black")
signal_receiver_passed = State("SignalReceiverPassed", signal_full_accept_color, "⚡⇉", "black")
signal_receiver_reset = State("SignalReceiverReset", waiting_color, "⚡↺", "black")
signal_receiver_states = [signal_receiver_inactive, signal_received_accept, signal_received_reject, signal_receiver_passed, signal_receiver_reset]

signal_transmitter = State("SignalTransmitter", signal_active_color, "⇉⍼", "black")
signal_transmitter_inactive = State("SignalTransmitterInactive", signal_inactive_color, "⍼", "black")
signal_transmitter_reset = State("SignalTransmitterReset", reset_color, "⍼↺", "black")
signal_transmitter_accept = State("SignalTransmitterAccept", signal_full_accept_color, "⍼✔", "black")
signal_transmitter_reject = State("SignalTransmitterReject", reject_color, "⍼✖ ", "black")
signal_transmitter_states = [signal_transmitter, signal_transmitter_reset,
                             signal_transmitter_inactive, signal_transmitter_accept, signal_transmitter_reject]
signal_wire_inactive = State("SignalWireInactive", signal_inactive_color, "⚡⇉", "black")
signal_wire_active = State("SignalWireActive", signal_active_color, "⚡⇉", "black")

signal_wire_states = [signal_wire_inactive, signal_wire_active]

signal_start_checks_inactive = State("SignalStartChecksInactive", signal_inactive_color, "⏯")
signal_start_checks_active = State("SignalStartChecksActive", signal_full_accept_color, "⏯")
signal_end_checks_inactive = State("SignalEndChecksInactive", signal_inactive_color, "⚡")
signal_end_checks_accept = State("SignalEndChecksAccept", signal_full_accept_color, "✔✔")
signal_end_checks_reject = State("SignalEndChecksReject", reject_color, "✖")
signal_checks_states = [signal_start_checks_inactive, signal_start_checks_active, signal_end_checks_inactive, signal_end_checks_accept, signal_end_checks_reject]

signal_conditional_inactive = State(
    "SignalConditionalInactive", signal_inactive_color, "⍼⏱")
signal_conditional_waiting = State(
    "SignalConditionalWaiting", waiting_color, "⍼⏱")
signal_conditional_intermediate_accept = State(
    "SignalConditionalInterimAccept", activate_next_color, "⍼✔")
signal_conditional_full_accept = State(
    "SignalConditionalFullAccept", full_accept_color, "⍼✔✔")
signal_conditional_reject = State(
    "SignalConditionalReject", reject_color, "⍼✖")
signal_conditional_reset = State("SignalConditionalReset", reset_color, "⍼↺")

signal_conditional_states = [signal_conditional_inactive, signal_conditional_waiting, signal_conditional_intermediate_accept, signal_conditional_full_accept, signal_conditional_reject, signal_conditional_reset]
"""

✑𝗦
✑𝗡
✑[
✑]
✑(
✑)
✑0
✑1

"""
