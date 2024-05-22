### Rentals

Manage Rentals in Frappe. This Frappe app helps manage car rentals. The app includes the following main DocTypes

- `Driver`: Manages information about drivers.
- `Vehicle`: Manages information about vehicles
- `Ride Order`: Manages information about ride orders.
- `Ride Bookings`: Manages information about ride bookings.

## DocTypes

### Driver

The `Driver` DocType is used to manage and track individual drivers. It includes the following fields:

- **First Name**: First name of the driver.
- **Last Name**: Last name of the driver.
- **License Number**: License number of the driver.
- **Full Name**: The full name of the driver derived from the first name and the last name.
- **Phone Number**: The phone number of the driver.
- **Profile Image**: The image of the driver.

### Vehicle

The `Vehicle` DocType is used to manage and track individual vehicles. It includes the following fields:

- **Make**: make of the car e.g BMW.
- **Model**: The specific model of the car e.g M3.
- **Year**: The year in which the car was manufactured.
- **Title**: The title of the car generated dynamically from the make, model and year.
- **Color**: The color of the car.
- **Insurance Expiry**: The date of expiry of the car insurance.
- **Type**: The type of car e.g SUV, Sedan.
- **License plate**: The license plate of the car.
- **Vehicle Image**: The image of the car
- **Status**: The status of the car e.g Active, Out of Service.
- **Condition**: A rate field.
- **Audit Completed**: A check field modified by a vehicle auditor.
- **Is Published**: A check field that determines whether the form is published.

### Ride Order

The `Ride Order` DocType is used to manage and track individual ride orders. It includes the following fields:

- **Customer Name**: The name of the customer.
- **Contact Number**: The phone number of the passenger.
- **Pickup Time**: Refers to the time a customer would like to be picked up.
- **License Number**: License number of the driver.
- **Vehicle**: The vehicle desired by the customer.

### Ride Booking

The `Ride Booking` DocType is used to manage and track individual ride bookings. It includes the following fields:

- **Order**: Selected from the a list of orders.
- **Vehicle**: The vehicle desired by the customer.
- **Driver**: The desired driver.
- **Rate**: Refers to the amount charged per kilometer.
- **Items**: Table to a child doctype.
- **Total Amount**: The total amount charged for the booking.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch main
bench install-app rentals
```

### Tests

This app includes automated tests to ensure functionality. To run the tests, use the following command:

```bench --site irfan.cabs run-tests --app rentals

```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/rentals
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

### License

mit
