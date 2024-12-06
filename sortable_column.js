import 'https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.15.3/Sortable.min.js'

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
               // Using a handle would more secure as only elements with the class drop_handle can be moved.
               //  handle: ".drop_handle",
                ghostClass: 'opacity-50',
                onEnd: (evt) => this.$emit("item-drop", {
                    new_index: evt.newIndex,
                    old_index: evt.oldIndex,
                    new_list: parseInt(evt.to.id.slice(1)),
                    old_list: parseInt(evt.from.id.slice(1)),
                }),
            });
        },
    },
};