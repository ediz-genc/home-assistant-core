export const id=5588;export const ids=[5588];export const modules={42946:(e,t,i)=>{i.d(t,{d:()=>n});const n=e=>e.stopPropagation()},27783:(e,t,i)=>{var n=i(36312),a=i(68689),o=i(30116),s=i(43389),r=i(66360),d=i(29818);(0,n.A)([(0,d.EM)("ha-list-item")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"method",key:"renderRipple",value:function(){return this.noninteractive?"":(0,a.A)(i,"renderRipple",this,3)([])}},{kind:"get",static:!0,key:"styles",value:function(){return[s.R,r.AH`:host{padding-left:var(--mdc-list-side-padding-left,var(--mdc-list-side-padding,20px));padding-inline-start:var(--mdc-list-side-padding-left,var(--mdc-list-side-padding,20px));padding-right:var(--mdc-list-side-padding-right,var(--mdc-list-side-padding,20px));padding-inline-end:var(--mdc-list-side-padding-right,var(--mdc-list-side-padding,20px))}:host([graphic=avatar]:not([twoLine])),:host([graphic=icon]:not([twoLine])){height:48px}span.material-icons:first-of-type{margin-inline-start:0px!important;margin-inline-end:var(--mdc-list-item-graphic-margin,16px)!important;direction:var(--direction)!important}span.material-icons:last-of-type{margin-inline-start:auto!important;margin-inline-end:0px!important;direction:var(--direction)!important}.mdc-deprecated-list-item__meta{display:var(--mdc-list-item-meta-display);align-items:center;flex-shrink:0}:host([graphic=icon]:not([twoline])) .mdc-deprecated-list-item__graphic{margin-inline-end:var(--mdc-list-item-graphic-margin,20px)!important}:host([multiline-secondary]){height:auto}:host([multiline-secondary]) .mdc-deprecated-list-item__text{padding:8px 0}:host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text{text-overflow:initial;white-space:normal;overflow:auto;display:inline-block;margin-top:10px}:host([multiline-secondary]) .mdc-deprecated-list-item__primary-text{margin-top:10px}:host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text::before{display:none}:host([multiline-secondary]) .mdc-deprecated-list-item__primary-text::before{display:none}:host([disabled]){color:var(--disabled-text-color)}:host([noninteractive]){pointer-events:unset}`,"rtl"===document.dir?r.AH`span.material-icons:first-of-type,span.material-icons:last-of-type{direction:rtl!important;--direction:rtl}`:r.AH``]}}]}}),o.J)},67383:(e,t,i)=>{var n=i(36312),a=i(68689),o=i(24500),s=i(14691),r=i(66360),d=i(29818),l=i(46530),c=i(37968);i(58715);(0,n.A)([(0,d.EM)("ha-select")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,d.MZ)({type:Boolean})],key:"icon",value:()=>!1},{kind:"field",decorators:[(0,d.MZ)({type:Boolean,reflect:!0})],key:"clearable",value:()=>!1},{kind:"method",key:"render",value:function(){return r.qy` ${(0,a.A)(i,"render",this,3)([])} ${this.clearable&&!this.required&&!this.disabled&&this.value?r.qy`<ha-icon-button label="clear" @click="${this._clearValue}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button>`:r.s6} `}},{kind:"method",key:"renderLeadingIcon",value:function(){return this.icon?r.qy`<span class="mdc-select__icon"><slot name="icon"></slot></span>`:r.s6}},{kind:"method",key:"connectedCallback",value:function(){(0,a.A)(i,"connectedCallback",this,3)([]),window.addEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.A)(i,"disconnectedCallback",this,3)([]),window.removeEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"_clearValue",value:function(){!this.disabled&&this.value&&(this.valueSetDirectly=!0,this.select(-1),this.mdcFoundation.handleChange())}},{kind:"field",key:"_translationsUpdated",value(){return(0,l.s)((async()=>{await(0,c.E)(),this.layoutOptions()}),500)}},{kind:"field",static:!0,key:"styles",value:()=>[s.R,r.AH`:host([clearable]){position:relative}.mdc-select:not(.mdc-select--disabled) .mdc-select__icon{color:var(--secondary-text-color)}.mdc-select__anchor{width:var(--ha-select-min-width,200px)}.mdc-select--filled .mdc-select__anchor{height:var(--ha-select-height,56px)}.mdc-select--filled .mdc-floating-label{inset-inline-start:12px;inset-inline-end:initial;direction:var(--direction)}.mdc-select--filled.mdc-select--with-leading-icon .mdc-floating-label{inset-inline-start:48px;inset-inline-end:initial;direction:var(--direction)}.mdc-select .mdc-select__anchor{padding-inline-start:12px;padding-inline-end:0px;direction:var(--direction)}.mdc-select__anchor .mdc-floating-label--float-above{transform-origin:var(--float-start)}.mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,0px)}:host([clearable]) .mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,12px)}ha-icon-button{position:absolute;top:10px;right:28px;--mdc-icon-button-size:36px;--mdc-icon-size:20px;color:var(--secondary-text-color);inset-inline-start:initial;inset-inline-end:28px;direction:var(--direction)}`]}]}}),o.o)},65588:(e,t,i)=>{i.r(t),i.d(t,{HaConversationAgentSelector:()=>y});var n=i(36312),a=i(66360),o=i(29818),s=i(68689),r=(i(253),i(94438),i(16891),i(50880)),d=i(42946),l=i(46530),c=i(37880);var p=i(29371);const h=(e,t)=>e.callApi("POST","config/config_entries/options/flow",{handler:t,show_advanced_options:Boolean(e.userData?.showAdvanced)}),u=(e,t)=>e.callApi("GET",`config/config_entries/options/flow/${t}`),m=(e,t,i)=>e.callApi("POST",`config/config_entries/options/flow/${t}`,i),g=(e,t)=>e.callApi("DELETE",`config/config_entries/options/flow/${t}`);var v=i(78897);i(27783),i(67383);var _=i(8257);const f="__NONE_OPTION__";(0,n.A)([(0,o.EM)("ha-conversation-agent-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,o.MZ)()],key:"language",value:void 0},{kind:"field",decorators:[(0,o.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.MZ)({type:Boolean,reflect:!0})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,o.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,o.wk)()],key:"_agents",value:void 0},{kind:"field",decorators:[(0,o.wk)()],key:"_configEntry",value:void 0},{kind:"method",key:"render",value:function(){if(!this._agents)return a.s6;let e=this.value;if(!e&&this.required){for(const t of this._agents)if("conversation.home_assistant"===t.id&&t.supported_languages.includes(this.language)){e=t.id;break}if(!e)for(const t of this._agents)if("*"===t.supported_languages&&t.supported_languages.includes(this.language)){e=t.id;break}}return e||(e=f),a.qy` <ha-select .label="${this.label||this.hass.localize("ui.components.coversation-agent-picker.conversation_agent")}" .value="${e}" .required="${this.required}" .disabled="${this.disabled}" @selected="${this._changed}" @closed="${d.d}" fixedMenuPosition naturalMenuWidth> ${this.required?a.s6:a.qy`<ha-list-item .value="${f}"> ${this.hass.localize("ui.components.coversation-agent-picker.none")} </ha-list-item>`} ${this._agents.map((e=>a.qy`<ha-list-item .value="${e.id}" .disabled="${"*"!==e.supported_languages&&0===e.supported_languages.length}"> ${e.name} </ha-list-item>`))}</ha-select>${this._configEntry?.supports_options?a.qy`<ha-icon-button .path="${"M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"}" @click="${this._openOptionsFlow}"></ha-icon-button>`:""} `}},{kind:"method",key:"willUpdate",value:function(e){(0,s.A)(i,"willUpdate",this,3)([e]),this.hasUpdated?e.has("language")&&this._debouncedUpdateAgents():this._updateAgents(),e.has("value")&&this._maybeFetchConfigEntry()}},{kind:"method",key:"_maybeFetchConfigEntry",value:async function(){if(this.value&&this.value in this.hass.entities)try{const e=await(0,_.v)(this.hass,this.value);if(!e.config_entry_id)return void(this._configEntry=void 0);this._configEntry=(await(0,c.Vx)(this.hass,e.config_entry_id)).config_entry}catch(e){this._configEntry=void 0}else this._configEntry=void 0}},{kind:"field",key:"_debouncedUpdateAgents",value(){return(0,l.s)((()=>this._updateAgents()),500)}},{kind:"method",key:"_updateAgents",value:async function(){const{agents:e}=await(t=this.hass,i=this.language,n=this.hass.config.country||void 0,t.callWS({type:"conversation/agent/list",language:i,country:n}));var t,i,n;if(this._agents=e,!this.value)return;const a=e.find((e=>e.id===this.value));(0,r.r)(this,"supported-languages-changed",{value:a?.supported_languages}),(!a||"*"!==a.supported_languages&&0===a.supported_languages.length)&&(this.value=void 0,(0,r.r)(this,"value-changed",{value:this.value}))}},{kind:"method",key:"_openOptionsFlow",value:async function(){var e,t,i;this._configEntry&&(e=this,t=this._configEntry,i={manifest:await(0,p.QC)(this.hass,this._configEntry.domain)},(0,v.g)(e,{startFlowHandler:t.entry_id,domain:t.domain,...i},{flowType:"options_flow",loadDevicesAndAreas:!1,createFlow:async(e,i)=>{const[n]=await Promise.all([h(e,i),e.loadFragmentTranslation("config"),e.loadBackendTranslation("options",t.domain),e.loadBackendTranslation("selector",t.domain)]);return n},fetchFlow:async(e,i)=>{const[n]=await Promise.all([u(e,i),e.loadFragmentTranslation("config"),e.loadBackendTranslation("options",t.domain),e.loadBackendTranslation("selector",t.domain)]);return n},handleFlowStep:m,deleteFlow:g,renderAbortDescription(e,i){const n=e.localize(`component.${i.translation_domain||t.domain}.options.abort.${i.reason}`,i.description_placeholders);return n?a.qy` <ha-markdown breaks allowsvg .content="${n}"></ha-markdown> `:i.reason},renderShowFormStepHeader:(e,i)=>e.localize(`component.${i.translation_domain||t.domain}.options.step.${i.step_id}.title`,i.description_placeholders)||e.localize("ui.dialogs.options_flow.form.header"),renderShowFormStepDescription(e,i){const n=e.localize(`component.${i.translation_domain||t.domain}.options.step.${i.step_id}.description`,i.description_placeholders);return n?a.qy` <ha-markdown allowsvg breaks .content="${n}"></ha-markdown> `:""},renderShowFormStepFieldLabel(e,i,n,a){if("expandable"===n.type)return e.localize(`component.${t.domain}.options.step.${i.step_id}.sections.${n.name}.name`);const o=a?.path?.[0]?`sections.${a.path[0]}.`:"";return e.localize(`component.${t.domain}.options.step.${i.step_id}.${o}data.${n.name}`)||n.name},renderShowFormStepFieldHelper(e,i,n,o){if("expandable"===n.type)return e.localize(`component.${i.translation_domain||t.domain}.options.step.${i.step_id}.sections.${n.name}.description`);const s=o?.path?.[0]?`sections.${o.path[0]}.`:"",r=e.localize(`component.${i.translation_domain||t.domain}.options.step.${i.step_id}.${s}data_description.${n.name}`,i.description_placeholders);return r?a.qy`<ha-markdown breaks .content="${r}"></ha-markdown>`:""},renderShowFormStepFieldError:(e,i,n)=>e.localize(`component.${i.translation_domain||t.domain}.options.error.${n}`,i.description_placeholders)||n,renderShowFormStepFieldLocalizeValue:(e,i,n)=>e.localize(`component.${t.domain}.selector.${n}`),renderShowFormStepSubmitButton:(e,i)=>e.localize(`component.${t.domain}.options.step.${i.step_id}.submit`)||e.localize("ui.panel.config.integrations.config_flow."+(!1===i.last_step?"next":"submit")),renderExternalStepHeader:(e,t)=>"",renderExternalStepDescription:(e,t)=>"",renderCreateEntryDescription:(e,t)=>a.qy` <p>${e.localize("ui.dialogs.options_flow.success.description")}</p> `,renderShowFormProgressHeader:(e,i)=>e.localize(`component.${t.domain}.options.step.${i.step_id}.title`)||e.localize(`component.${t.domain}.title`),renderShowFormProgressDescription(e,i){const n=e.localize(`component.${i.translation_domain||t.domain}.options.progress.${i.progress_action}`,i.description_placeholders);return n?a.qy` <ha-markdown allowsvg breaks .content="${n}"></ha-markdown> `:""},renderMenuHeader:(e,i)=>e.localize(`component.${t.domain}.options.step.${i.step_id}.title`)||e.localize(`component.${t.domain}.title`),renderMenuDescription(e,i){const n=e.localize(`component.${i.translation_domain||t.domain}.options.step.${i.step_id}.description`,i.description_placeholders);return n?a.qy` <ha-markdown allowsvg breaks .content="${n}"></ha-markdown> `:""},renderMenuOption:(e,i,n)=>e.localize(`component.${i.translation_domain||t.domain}.options.step.${i.step_id}.menu_options.${n}`,i.description_placeholders),renderLoadingDescription:(e,i)=>e.localize(`component.${t.domain}.options.loading`)||("loading_flow"===i||"loading_step"===i?e.localize(`ui.dialogs.options_flow.loading.${i}`,{integration:(0,p.p$)(e.localize,t.domain)}):"")}))}},{kind:"get",static:!0,key:"styles",value:function(){return a.AH`:host{display:flex;align-items:center}ha-select{width:100%}ha-icon-button{color:var(--secondary-text-color)}`}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===f||(this.value=t.value===f?void 0:t.value,(0,r.r)(this,"value-changed",{value:this.value}),(0,r.r)(this,"supported-languages-changed",{value:this._agents.find((e=>e.id===this.value))?.supported_languages}))}}]}}),a.WF);let y=(0,n.A)([(0,o.EM)("ha-selector-conversation_agent")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.MZ)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,o.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,o.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,o.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,o.MZ)({type:Boolean})],key:"required",value:()=>!0},{kind:"field",decorators:[(0,o.MZ)({attribute:!1})],key:"context",value:void 0},{kind:"method",key:"render",value:function(){return a.qy`<ha-conversation-agent-picker .hass="${this.hass}" .value="${this.value}" .language="${this.selector.conversation_agent?.language||this.context?.language}" .label="${this.label}" .helper="${this.helper}" .disabled="${this.disabled}" .required="${this.required}"></ha-conversation-agent-picker>`}},{kind:"field",static:!0,key:"styles",value:()=>a.AH`ha-conversation-agent-picker{width:100%}`}]}}),a.WF)},8257:(e,t,i)=>{i.d(t,{jh:()=>o,Ox:()=>r,P9:()=>d,v:()=>s});i(253),i(2075),i(94438);var n=i(94100),a=i(81523);i(82739);const o=(e,t)=>{if(t.name)return t.name;const i=e.states[t.entity_id];return i?(0,a.u)(i):t.original_name?t.original_name:t.entity_id},s=(e,t)=>e.callWS({type:"config/entity_registry/get",entity_id:t}),r=(0,n.A)((e=>{const t={};for(const i of e)t[i.entity_id]=i;return t})),d=(0,n.A)((e=>{const t={};for(const i of e)t[i.id]=i;return t}))},29371:(e,t,i)=>{i.d(t,{QC:()=>o,fK:()=>a,p$:()=>n});const n=(e,t,i)=>e(`component.${t}.title`)||i?.name||t,a=(e,t)=>{const i={type:"manifest/list"};return t&&(i.integrations=t),e.callWS(i)},o=(e,t)=>e.callWS({type:"manifest/get",integration:t})},78897:(e,t,i)=>{i.d(t,{g:()=>o});var n=i(50880);const a=()=>Promise.all([i.e(4131),i.e(668),i.e(9815),i.e(3549),i.e(4035)]).then(i.bind(i,74035)),o=(e,t,i)=>{(0,n.r)(e,"show-dialog",{dialogTag:"dialog-data-entry-flow",dialogImport:a,dialogParams:{...t,flowConfig:i,dialogParentElement:e}})}}};
//# sourceMappingURL=5588.jh4GLwtZCZE.js.map