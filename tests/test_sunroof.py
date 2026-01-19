# tests/test_sunroof.py
import pytest
import sys
import os

# This line is needed to find the 'src' folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sunroof_controller import SunroofController

# Fixture: This runs before every test function (like 'SetUp' in manual testing)
@pytest.fixture
def ecu():
    return SunroofController()

def test_initial_state(ecu):
    """Requirement: System must start in CLOSED state"""
    assert ecu.get_status() == "CLOSED"

def test_open_sunroof_success(ecu):
    """Requirement: Sending OPEN command should change state to OPEN"""
    result = ecu.open_sunroof()
    assert result == "SUCCESS"
    assert ecu.get_status() == "OPEN"

def test_close_sunroof_success(ecu):
    """Requirement: Sending CLOSE command should change state to CLOSED"""
    # First we open it
    ecu.open_sunroof()
    
    # Then we close it
    result = ecu.close_sunroof()
    assert result == "SUCCESS"
    assert ecu.get_status() == "CLOSED"

def test_safety_lock_feature(ecu):
    """Requirement: Sunroof must NOT open if vehicle is locked"""
    ecu.lock_vehicle()
    
    # Try to open
    result = ecu.open_sunroof()
    
    # Validation
    assert result == "ERROR_LOCKED"
    assert ecu.get_status() == "CLOSED"  # Should remain closed