function CartItemHandler($rootScope) {

    // initialization
    var cartItems = $rootScope.cartItems;


    this.getCartSize = function getCartSize() {
        return cartItems.length;
    };

    this.removeProduct = function removeProduct() {
        return cartItems.length;
    };

    this.addProduct = function setProduct(product) {
        return cartItems.push(product);
    };

    this.getProduct = function getProduct(productID) {
        return cartItems.length;
    };


    this.getCartPrice = function getCartPrice() {
        var cartPrice;
        for (var i = 0; i < getCartSize(); i++) {
            cartPrice += cartItems[i].price
        }
        return cartPrice;
    };


    this.checkProductInCart = function checkProductInCart(productID) {
        return cartItems.length;
    };


}