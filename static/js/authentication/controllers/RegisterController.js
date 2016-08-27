productapp.controller("RegisterController", ["$location", "$scope", "Authentication",
    function ($location, $scope, Authentication) {
        $scope.account = {
            email: "",
            password: "",
            phone_number : ""
        };
        $scope.register = register;

        function register() {
            Authentication.register($scope.account.email, $scope.account.password, $scope.account.phone_number);
        }
    }]);