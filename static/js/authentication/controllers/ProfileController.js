
productapp.controller("ProfileController", ["$location", "$scope", "Authentication", function ($location, $scope, Authentication) {

    $scope.showProfileUpdateSuccessMessage = false;

    var profile = {
        firstName: "",
        lastName: "",
        email: "",
        phoneNumber: "",
        alternatePhoneNumber: "",
        addressOne: "",
        addressTwo: "",
        street: "",
        city: "",
        district: "",
        state: "",
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
        $scope.profile.companyName = profileAPIData.company;
        $scope.profile.phoneNumber = profileAPIData.phonenumber;
        // $scope.profile.password = profileAPIData.password;

        $scope.profile.alternetPhoneNumber = profileAPIData.phonenumber_two;
        $scope.profile.addressOne = profileAPIData.address_one;
        $scope.profile.addressTwo = profileAPIData.address_two;
        $scope.profile.street = profileAPIData.street;
        $scope.profile.city = profileAPIData.city;
        $scope.profile.district = profileAPIData.district;
        $scope.profile.state = profileAPIData.state;


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
