% Load the data
load('data.mat');

% Access the field 'd' from the struct 'd' in your loaded data
data_values = d.d;

% Plot the data
plot(data_values);
xlabel('Index');
ylabel('Value');
title('Plot of d');
grid on;
