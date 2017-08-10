(function() {
	'use strict';

	angular.module('career.demo', [])
		.controller('CareerController', ['$scope', '$http', CareerController]);

	function CareerController($scope, $http){
		$scope.person = {
			name: 'Joe',
			age: 35
		};
		$scope.data =[]
		$http.get('/careers/categories/').then(function(response)
		{
			$scope.data = response.data
		})
	}
}());