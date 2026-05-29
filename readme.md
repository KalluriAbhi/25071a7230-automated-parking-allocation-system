# 🚗 Automated Parking Allocation System

A lightweight, interactive Command Line Interface (CLI) application built in Python to automate vehicle parking management. The system supports multi-floor tracking, automatic slot allocation, dynamic duration-based billing calculation, and real-time layout visualization.

---

## 🌟 Features

- **Multi-Floor Matrix Tracking:** Pre-configured with a 2-floor, 3-slots-per-floor structural layout (easily scalable).
- **First-Available Slot Allocation:** Automatically finds and books the nearest empty slot starting from Floor 1.
- **Smart Ceiling Billing Logic:** Tracks entry/exit timestamps via Python's `datetime` module and automatically rounds any fraction of an hour up to the next full hour.
- **Real-Time Layout Visualization:** Provides a transparent overview of which parking bays are `EMPTY` vs. `OCCUPIED` along with the assigned vehicle plates.
- **Multiple Payment Frameworks:** Supports logging transactions through UPI, Cash, or Card variants.

---

## 🛠️ System Workflow

The system cycles continuously through an interactive runtime menu split across 5 major core stages:

1. **System Initialization:** Memory builds a structured matrix dictionary tracking variables like occupant names, contact phones, vehicle strings, and exact time arrays.
2. **Layout Audit:** Displays your infrastructure configurations showing vacant and taken nodes.
3. **Reservation:** Captures data schemas and assigns the target location index smoothly.
4. **Tariff Clearance:** Compares total elapsed seconds, triggers manual ceiling calculation rules, structures an official receipt, and releases the slot block back to the pool.
5. **Termination:** Destroys active loop indices gracefully via standard execution breaks.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your local machine.

### Installation & Execution
1. Clone this repository or download the source script file:
   ```bash
   git clone [https://github.com/your-username/automated-parking-system.git](https://github.com/your-username/automated-parking-system.git)
   cd automated-parking-system
