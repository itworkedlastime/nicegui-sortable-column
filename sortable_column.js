import 'https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.15.0/Sortable.min.js'

export default {
  template: `
    <div>
      <slot></slot>
    </div>
  `,
  props: {
    group: String,
  },
  mounted() {
    this.makesortable();
  },
  methods: {
    makesortable() {
      if (this.group === 'None') {
      this.group = this.$el.id;
      }
      Sortable.create(this.$el, {
      group: this.group,
      animation: 150,
      ghostClass: 'opacity-50',
      onEnd: (evt) => this.$emit("item-drop", {
        parent: parseInt(this.$el.id.slice(1)),
        id: parseInt(evt.item.id.slice(1)),
        new_index: evt.newIndex,
        new_list: evt.to,
        old_list: evt.from,
        event: evt,
      }),
      });
    },
  },
};
