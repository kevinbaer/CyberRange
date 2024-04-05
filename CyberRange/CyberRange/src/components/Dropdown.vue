<template>
  <div class="dropdown">
    <component
      :is="toggleTag"
      class="dropdown-toggle"
      :class="{ [`btn-${variant}`]: Boolean(variant), [toggleClass]: true }"
      data-bs-toggle="dropdown"
      ref="toggle"
    >
      <slot name="toggle">Action</slot>
    </component>
    <component
      :is="menuTag"
      class="dropdown-menu position-fixed"
      :class="menuClass"
      ref="menu"
    >
      <slot />
    </component>
  </div>
</template>
<script>
import { Dropdown } from "bootstrap";
const propDefaults = {
  menuTag: "ul",
  menuClass: "",
  toggleTag: "button",
  toggleClass: "btn",
  variant: "outline-secondary",
};
export default {
  props: Object.assign(
    {},
    ...Object.entries(propDefaults).map(([key, value]) => ({
      [key]: {
        type: String,
        default: value,
      },
    }))
  ),
  data: () => ({
    show: false,
  }),
  mounted() {
    window.addEventListener("click", this.move);
    new Dropdown(this.$refs.toggle);
  },
  beforeUnmount() {
    window.removeEventListener("click", this.move);
  },
  methods: {
    toggle() {
      this.show = !this.show;
    },
    move(e) {
      const { menu, toggle: trigger } = this.$refs;
      if (this.show) {
        this.toggle();
        this.$el.appendChild(menu);
      } else {
        if (e.target.closest(".dropdown-toggle") === trigger) {
          this.$nextTick(() => {
            this.toggle();
            document.body.appendChild(menu);
          });
        }
      }
    },
  },
};
</script>
