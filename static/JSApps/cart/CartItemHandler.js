function CartItemHandler($rootScope) {

    // initialization
    var cartItems = $rootScope.cartItems;


    this.getCartSize = function getCartSize() {
        return cartItems.length;
    };

    this.removeProduct = function removeProduct(product) {
         var productExistIndex = getProductExistIndexUsingProductID(product.product_id);

        if (productExistIndex !== -1) {
            var existingProduct = cartItems[productExistIndex];
            if (existingProduct.totalQuantity>0) {
                existingProduct.totalQuantity-=1
            } else {
               cartItems.splice(productExistIndex, 1);
            }

        } else {
             // product is not found in cart
        }
    };

    this.addProduct = function setProduct(product, rateOfSelectedPackSize, totalQuantity) {
        console.log("in cart add");
        var productExistIndex = getProductExistIndexUsingProductID(product.product_id);

        if (productExistIndex === -1) {
            cartItems.push(product);
        }
        else {
            var existingProduct = cartItems[productExistIndex];
            existingProduct.totalQuantity = totalQuantity;
            existingProduct.rateOfSelectedPackSize = rateOfSelectedPackSize;
        }
    };

    this.getProduct = function getProduct(product_id) {
        var productExistIndex = getProductExistIndexUsingProductID(product_id);
         if (productExistIndex === -1) {
            return null;
        }
        else {
            return cartItems[productExistIndex]
        }
    };


    this.getCartPrice = function getCartPrice() {
        var cartPrice=0;
        console.log("in price");
        console.log(this.getCartSize());
        for (var i = 0; i < this.getCartSize(); i++) {
            console.log(cartPrice);
            console.log(cartItems[i].rateOfSelectedPackSize);
            console.log(cartItems[i].totalQuantity);

            cartPrice = cartPrice + cartItems[i].rateOfSelectedPackSize * cartItems[i].totalQuantity
        }
        return cartPrice;
    };


    this.checkProductInCart = function checkProductInCart(productID) {
        return cartItems.length;
    };

    function getProductExistIndexUsingProductID(product_id) {
          var productExistIndex = -1;

        //Find product using product_id
         for (var i = 0; i < cartItems.length; i++) {
            if (product_id === cartItems[i].product_id) {
                productExistIndex = i;
            }
        }
        return productExistIndex
    }
}