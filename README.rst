Home Assistant |Chat Status|
=================================================================================

Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.

# Home Assistant Spotify Integration and Setup Guide

This guide provides detailed instructions for setting up and customizing Home Assistant with updated Spotify integration and related features.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Directory Overview](#directory-overview)
- [Key Plugins and Components](#key-plugins-and-components)
  - [HACS](#hacs)
  - [Spotcast](#spotcast)
  - [Spotify Integration](#spotify-integration)
  - [Interface Preparation](#interface-preparation)
- [Testing the Setup](#testing-the-setup)
- [Important Notes](#important-notes)

---

## Prerequisites
1. **Python 3.13**:
   - Update your Python installation to version **3.13**.
   - Recreate the virtual environment:
     ```bash
     rm -rf venv
     python3.13 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

2. **Home Assistant Configuration**:
   - Familiarize yourself with the `configuration.yaml` file as it contains most of the changes.
   - Ensure your environment is updated with the latest Home Assistant core changes.

---

## Environment Setup
1. **Run the Core**:
   - Start Home Assistant with the updated setup.
   - Ensure all dependencies and integrations are correctly configured.

2. **Directories**:
   - **`custom_components`**: Contains custom integrations (e.g., Spotify, Spotcast). If issues occur, delete and reinstall components here.
   - **`www`**: Hosts visual plugins, panels, and cards. Manage them via:
     - `settings -> integration -> top right menu -> resources`.
   - **`secrets.yaml`**: Stores sensitive configuration data (e.g., Spotify keys).

---

## Key Plugins and Components

### HACS
- **Purpose**: Simplifies plugin installation and management.
- **Installation**:
  - Follow the official [HACS installation guide](https://www.hacs.xyz/).
  - Once configured, access the HACS dashboard from the Home Assistant sidebar.

---

### Spotcast
- **Purpose**: Manage Spotify requests and control Spotify Connect devices.
- **Installation**:
  1. Install via HACS or follow the [Spotcast GitHub documentation](https://github.com/fondberg/spotcast/tree/v4.0.0).
  2. Configure `secrets.yaml`:
     ```yaml
     sp_dc: YOUR_SP_DC_KEY
     sp_key: YOUR_SP_KEY
     ```
     - Retrieve `sp_dc` and `sp_key`:
       - Open Spotify Web and extract these from cookies (keep the web page open to avoid cookie expiration).

- **Testing**:
  - Enable Advanced Mode in Home Assistant.
  - Navigate to `Developer Tools -> Action -> Spotcast: Start Spotcast`.
  - Use `device_id` for reliable endpoint configuration. Fetch device IDs from [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/get-a-users-available-devices).

---

### Spotify Integration
- **Purpose**: Replace the default Spotify integration with an updated, feature-rich version.
- **Requirements**:
  - A Spotify Premium account is required.
- **Setup**:
  1. Add the Spotify integration:
     - Navigate to `Settings -> Devices & Services -> Add Integration`.
  2. Configure:
     - Input your Spotify `device_loginid` from your [Spotify Profile](https://www.spotify.com/uk/account/profile/).

- **Verification**:
  - After setup, you should see a working media player card on the Home Assistant dashboard.

---

## Interface Preparation

### Install Plugins
- Use HACS to install:
  - **ApexCharts**: For advanced charting and visualizations.
  - **Button Card**: For creating customizable button controls.

### Create a Dashboard
1. Navigate to `Settings -> Dashboards -> Add Dashboards -> New from Scratch`.
2. Edit the dashboard:
   - Click the left panel, select the pencil icon (top-right).
   - Add cards by pasting configuration into the editor panel.

### Example Panel Code
Replace placeholders (e.g., names, configuration keys) in the provided panel code with your values:
- Use `developer tools -> states` to retrieve specific entity names.
- Adjust `configuration.yaml` accordingly.

---

## Testing the Setup
1. **Enable Advanced Mode**:
   - Navigate to your user profile and toggle on Advanced Mode.
2. **Testing Plugins**:
   - Test Spotcast from `Developer Tools -> Action`.
   - Validate Spotify media player functionality on the dashboard.
3. **Spotcast Endpoints**:
   - Use the `device_id` method for consistent endpoint results.

---

## Important Notes
1. **Custom Components**:
   - Files in `custom_components` override default integrations. If issues arise, delete and reinstall the component via HACS.
2. **Secrets Handling**:
   - Always store sensitive information (e.g., API keys) in `secrets.yaml`.
3. **Naming Conventions**:
   - Update placeholders in the configuration and dashboard files to match your specific setup.
4. **Debugging**:
   - Logs and debugging tools in Home Assistant can assist in resolving setup issues.

---

## Resources
- [Home Assistant Documentation](https://www.home-assistant.io/

Check out `home-assistant.io <https://home-assistant.io>`__ for `a
demo <https://demo.home-assistant.io>`__, `installation instructions <https://home-assistant.io/getting-started/>`__,
`tutorials <https://home-assistant.io/getting-started/automation/>`__ and `documentation <https://home-assistant.io/docs/>`__.

This is a project of the `Open Home Foundation <https://www.openhomefoundation.org/>`__.

|screenshot-states|

Featured integrations
---------------------

|screenshot-integrations|

The system is built using a modular approach so support for other devices or actions can be implemented easily. See also the `section on architecture <https://developers.home-assistant.io/docs/architecture_index/>`__ and the `section on creating your own
components <https://developers.home-assistant.io/docs/creating_component_index/>`__.

If you run into issues while using Home Assistant or during development
of a component, check the `Home Assistant help section <https://home-assistant.io/help/>`__ of our website for further help and information.

.. |Chat Status| image:: https://img.shields.io/discord/330944238910963714.svg
   :target: https://www.home-assistant.io/join-chat/
.. |screenshot-states| image:: https://raw.githubusercontent.com/home-assistant/core/dev/.github/assets/screenshot-states.png
   :target: https://demo.home-assistant.io
.. |screenshot-integrations| image:: https://raw.githubusercontent.com/home-assistant/core/dev/.github/assets/screenshot-integrations.png
   :target: https://home-assistant.io/integrations/
