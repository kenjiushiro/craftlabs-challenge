<script>
export default {
  data() {
    return {
      products: [],
    };
  },
  methods: {
    getProducts: function () {
      self = this;
      fetch("http://localhost:8000/products/", {
        method: "GET",
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (products) {
          console.log(products);
          self.products = products;
        });
    },
  },
  created() {
    this.getProducts();
  },
};
</script>

<template>
  <WelcomeItem>
    <template #heading>Products</template>

    <table>
      <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Category</th>
      </tr>
      <tr v-for="(product, index) of products" :key="product.id">
        <td>{{ product.fields.name }}</td>
        <td>{{ product.fields.price }}</td>
        <td>{{ product.fields.category }}</td>
      </tr>
    </table>
  </WelcomeItem>
</template>
