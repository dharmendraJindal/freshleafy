articlesapp.controller("LoginController", ["$location", "$scope", "Authentication",
    function ($location, $scope, Authentication) {
        $scope.account = {
            username: "",
            password: ""
        };
        $scope.login = login;
        activate();
        function activate() {
            if (Authentication.isAuthenticated()) {
                $location.url("/");
            }
        }

        function login() {
            Authentication.login($scope.account.username, $scope.account.password);
        }
    }]);