import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  click() {
    let fontId = this.get('font');
    if (fontId !== undefined) {
      this.get('sendDefFont')(fontId);
    }
  }
});
