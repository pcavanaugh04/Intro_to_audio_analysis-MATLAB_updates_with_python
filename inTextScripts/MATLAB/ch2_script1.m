% script1.m
% Demonstrate generation of synthetic tones

Fs = 16000; Ts = 1/Fs;         % Sampling freq, sampling period
time = 0:Ts:1;               % Define when sampling occurs (0.1 seconds)
Freqs = [250 550 900];         % Frequencies of desired signals

% Initialize matrix of zeros to populate signal values
Xs = zeros(length(Freqs), length(time));

% Signal generation
for i = 1:length(Freqs)
    Xs(i,:) = cos(2*pi*Freqs(i)*time);
end

% Sum all tones. x is a single row vector that adds the values of each
% column in Xs
x = sum(Xs);                   % Final sum of tones. Single row vect
x = x ./ max(abs(x));          % Normalize x

figure; plot(time, x); axis([0 time(end) -1 1]); 
xlabel('Time (sec)'); ylabel('Signal Amplitude.');
title("Simple 3-toned audio signal")