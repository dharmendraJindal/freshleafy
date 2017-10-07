function CartItemHandler($rootScope) {

    // initialization
    var cartItems;
    init($rootScope.cartItems);
    this.init = function init(cartItems) {
        cartItems = cartItems;
    };


    this.getCartSize = function getCartSize() {
        return cartItems.length;
    };

    this.removeProduct = function removeProduct() {
        return cartItems.length;
    };

    this.setProduct = function setProduct(product) {
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