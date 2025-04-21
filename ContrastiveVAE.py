import torch
import torch.nn as nn

#variational autoencoder w contrastive learning :)
class ContrastiveVAE(nn.Module):
    def __init__(self, latent_dim=64):
        super(ContrastiveVAE, self).__init__()
        self.latent_dim = latent_dim

        # Encoder CNN
        self.encoder_cnn = nn.Sequential(
            nn.Conv2d(1, 32, 4, 2, 1),  # (B, 32, 112, 112)
            nn.ReLU(),
            nn.Conv2d(32, 64, 4, 2, 1), # (B, 64, 56, 56)
            nn.ReLU(),
        )

        self.flattened_size = 64 * 56 * 56
        self.encoder_flatten = nn.Flatten()
        self.fc_mu = nn.Linear(self.flattened_size, latent_dim)
        self.fc_logvar = nn.Linear(self.flattened_size, latent_dim)

        # Decoder (not really using had from before)
        self.decoder_input = nn.Linear(latent_dim, self.flattened_size)
        self.decoder = nn.Sequential(
            nn.Unflatten(1, (64, 56, 56)),
            nn.ConvTranspose2d(64, 32, 4, 2, 1),  # (B, 32, 112, 112)
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, 4, 2, 1),   # (B, 1, 224, 224)
            nn.Sigmoid()
        )

    def encode(self, x):
        x = self.encoder_cnn(x)
        x = self.encoder_flatten(x)
        mu = self.fc_mu(x)
        logvar = self.fc_logvar(x)
        return mu, logvar

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z):
        x = self.decoder_input(z)
        x = self.decoder(x)
        return x

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        x_recon = self.decode(z)
        return x_recon, mu, logvar
    
    


