class ContentCardExample extends HTMLElement {
    // Whenever the state changes, a new `hass` object is set. Use this to
    // update your content.
    set hass(hass) {
      // Initialize the content if it's not there yet.
      if (!this.content) {
        this.innerHTML = `
          <ha-card header="Example-card">
            <div>
                <h2>Hello!</h2>
            </div>
          </ha-card>
        `;
        this.content = this.querySelector("div");
      }
  
      const entityId = this.config.entity;
      const state = hass.states[entityId];
      const stateStr = state ? state.state : "unavailable";
  
      this.content.innerHTML = 
      `
        <style>
          .media_player {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
          }
          .icons img {
            margin-top: 5px;
            width: 20px; /* Example size */
            height: 20px; /* Example size */
            cursor: pointer;
          }

          .songProgress {
            cursor: pointer;
          }
        </style>
        <div class= "media_player">
          <input type="range" name="range" id="songProgress" min="0" max="100">
          <div class="icons">
            <img src="/local/rewind-button.png" alt="Rewind Button" />
            <img src="/local/play.png" alt="Play Button" />
            <img src="/local/fast-forward.png" alt="Forward Button" />
          </div>
        </div>
      `;
    }
  
    // The user supplied configuration. Throw an exception and Home Assistant
    // will render an error card.
    setConfig(config) {
      if (!config.entity) {
        throw new Error("You need to define an entity");
      }
      this.config = config;
    }
  
    // The height of your card. Home Assistant uses this to automatically
    // distribute all cards over the available columns in masonry view
    getCardSize() {
      return 3;
    }
  
    // The rules for sizing your card in the grid in sections view
    getLayoutOptions() {
      return {
        grid_rows: 3,
        grid_columns: 2,
        grid_min_rows: 3,
        grid_max_rows: 3,
      };
    }
  }
  
  customElements.define("content-card-example", ContentCardExample);