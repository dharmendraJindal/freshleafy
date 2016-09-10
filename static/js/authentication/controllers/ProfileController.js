
productapp.controller("ProfileController", ["$location", "$scope", "Authentication", function ($location, $scope, Authentication) {

    $scope.showProfileUpdateSuccessMessage = false;

    var profile = {
        firstName: "",
        lastName: "",
        email: "",
        phone_number: "",
        companyName: ""
    };
    $scope.profile = angular.copy(profile);
    $scope.updateProfile = updateProfile;
    viewProfile();


    function viewProfile() {
        Authentication.getProfile().then(function (profileAPIData) {
            console.log(profileAPIData, 'pad');
            loadProfileData(profileAPIData);
        }, function () {
        });
    }

    function loadProfileData(profileAPIData) {
        
        $scope.profile.userID = profileAPIData.user_id;
        $scope.profile.firstName = profileAPIData.first_name ;
        $scope.profile.lastName = profileAPIData.last_name;
        $scope.profile.email = profileAPIData.email;
        $scope.profile.phone_number = profileAPIData.phonenumber;
        $scope.profile.companyName = profileAPIData.company

    }
    
    
    function updateProfile() {
        // if ($scope.ProfileForm.$invalid) {
        //     return false;
        // }
        console.log('in update fn');
        Authentication.updateProfile($scope.profile).then(function (data) {
            $scope.showProfileUpdateSuccessMessage = true;
            viewProfile();
        }, function () {
        });
    }
}]);
