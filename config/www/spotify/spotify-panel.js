import "https://unpkg.com/wired-card@2.1.0/lib/wired-card.js?module";
import { LitElement, html, css } from "https://unpkg.com/lit-element@2.4.0/lit-element.js?module";

class SpotifyPanel extends LitElement {
  static get properties() {
    return {
      hass: { type: Object },
      narrow: { type: Boolean },
      route: { type: Object },
      panel: { type: Object },
      spotifyEntity: { type: String },
      spotifyState: { type: Object },
    };
  }

  constructor() {
    super();
    this.spotifyEntity = this.getSpotifyEntity() || "media_player.spotify";
    this.spotifyState = null;
  }

  getSpotifyEntity() {
    if (!this.hass) {
      return null;
    }
  
    for (let entityId in this.hass.states) {
      if (entityId.startsWith("media_player.spotify")) {
        return entityId;
      }
    }
    return null;
  }

  updated(changedProperties) {
    super.updated(changedProperties);

    if (changedProperties.has("hass") && this.hass) {
      this.spotifyEntity = this.getSpotifyEntity() || "media_player.spotify";
      this.updateSpotifyState();
    }
  }

  updateSpotifyState() {
    if (this.hass && this.hass.states) {
      console.log("Current states:", this.hass.states);
      if (this.hass.states[this.spotifyEntity]) {
        this.spotifyState = this.hass.states[this.spotifyEntity];
      } else {
        this.spotifyState = null;
        console.warn(`Spotify entity (${this.spotifyEntity}) not found.`);
      }
    }
  }

  render() {
    return html`
      <wired-card elevation="2">
        <p>Spotify Listener Panel</p>
        ${this.spotifyState
          ? html`
              <p><b>Entity:</b> ${this.spotifyEntity}</p>
              <p><b>State:</b> ${this.spotifyState.state}</p>
              <p><b>Attributes:</b></p>
              <pre>${JSON.stringify(this.spotifyState.attributes, undefined, 2)}</pre>
            `
          : html`<p>Spotify entity not available.</p>`}
        <p>The screen is${this.narrow ? "" : " not"} narrow.</p>
      </wired-card>
    `;
  }

  static get styles() {
    return css`
      :host {
        background-color: #fafafa;
        padding: 16px;
        display: block;
      }
      wired-card {
        background-color: white;
        padding: 16px;
        display: block;
        font-size: 18px;
        max-width: 600px;
        margin: 0 auto;
      }
    `;
  }
}

customElements.define("spotify-panel", SpotifyPanel);