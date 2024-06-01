# Load required libraries
library(ggplot2)
library(dplyr)

# Load the dataset
df <- read.csv('Netflix_shows_movies/Netflix_shows_movies_cleaned.csv')

# Ensure the 'type' column is treated as a factor for ordered plotting
df$type <- factor(df$type, levels = df %>% count(type) %>% arrange(desc(n)) %>% pull(type))

# Plot the most watched genres
ggplot(df, aes(x = type)) + 
  geom_bar() + 
  coord_flip() + 
  labs(title = "Most Watched Genres", x = "Genre", y = "Count") +
  theme_minimal(base_size = 15) +
  theme(plot.title = element_text(hjust = 0.5))


