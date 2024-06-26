% script1.m
% Demonstrate generation of synthetic tones

Fs = 16000; Ts = 1/Fs;         % Sampling freq, sampling period
plot_time = 0:Ts:0.1;               % Define when sampling occurs (0.1 seconds)
play_time = 0:Ts:2;
Freqs = 2*[261.63 329.63 392];         % Frequencies of desired signals

% Initialize matrix of zeros to populate signal values
plot_Xs = zeros(length(Freqs), length(plot_time));
play_Xs = zeros(length(Freqs), length(play_time));

% Signal generation
for i = 1:length(Freqs)
    plot_Xs(i,:) = cos(2*pi*Freqs(i)*plot_time);
    play_Xs(i,:) = cos(2*pi*Freqs(i)*play_time);
end

% Sum all tones. x is a single row vector that adds the values of each
% column in Xs
plot_x = sum(plot_Xs);       % Final sum of tones. Single row vect
play_x = sum(play_Xs);

plot_x = plot_x ./ max(abs(plot_x));   % Normalize x
play_x = play_x ./ max(abs(play_x));   % Normalize x

figure;
subplot(4,1,1);
plot(plot_time, plot_Xs(1,:));
xlabel('Time (sec)'); ylabel('Signal Amplitude.');
title(string(Freqs(1)) + "Hz Signal");

subplot(4,1,2);
plot(plot_time, plot_Xs(2,:));
xlabel('Time (sec)'); ylabel('Signal Amplitude.');
title(string(Freqs(2)) + "Hz Signal");

subplot(4,1,3);
plot(plot_time, plot_Xs(3,:));
xlabel('Time (sec)'); ylabel('Signal Amplitude.');
title(string(Freqs(3)) + "Hz Signal");

subplot(4,1,4);
plot(plot_time, plot_x); axis([0 plot_time(end) -1 1]); 
xlabel('Time (sec)'); ylabel('Signal Amplitude.');
title("Resulting Signal");

sgtitle("3-toned audio signals")